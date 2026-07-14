from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class BlunderPolicyPassive(Passive):
    """Holder attacked, its effect flipped coins, any were tails: the owner
    draws 3 at the end of the turn (only while the tool is still in play)."""

    async def attack_followup(self, ctx, carrier):
        if carrier_pokemon(carrier) is not ctx.attacker:
            return
        if not any(r != 0 for r in ctx.coin_results):
            return
        await ctx.draw_cards(3)


card = PokemonToolCardDef(
    guid="98570270-fd4a-5b05-82c2-d8e03f008051",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlunderPolicy.Name",
    display_name="Blunder Policy",
    searchable_by=["Blunder Policy", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=131,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    passive=BlunderPolicyPassive(),
)
