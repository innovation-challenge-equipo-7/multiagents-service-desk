import ChatBubble from "./ChatBubble";
import LoadingIndicator from "./LoadingIndicator";


export default function ChatContainer({ messages, loading }) {
return (
<div className="flex flex-col gap-3 p-4 overflow-y-auto h-full">
{messages.map((m, index) => (
<ChatBubble key={index} text={m.text} from={m.from} />
))}


{loading && <LoadingIndicator />}
</div>
);
}