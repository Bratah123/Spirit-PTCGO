from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import Passive


class CraftsmanshipPassive(Passive):
    """This Pokemon gets +20 HP for each Fighting Energy attached to it."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier:
            return 0
        count = sum(
            1 for c in carrier.children
            if energy_provides_type(c, PokemonTypes.FIGHTING.value)
        )
        return 20 * count


async def top_down(ctx):
    """80. Flip until tails; discard opponent's top deck card per heads."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails(ctx.ability.title)
    if heads:
        await ctx.discard_cards(ctx.deck_top(heads, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="1571784c-d8fb-5211-9f69-23a8a874a394",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr", "Stage 2", "Conkeldurr"],
    subtypes=["Stage 2"],
    collector_number=64,
    set_code="BW3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    family_id=532,
    abilities=[
        Ability(
            title="Craftsmanship",
            game_text="This Pok\u00e9mon gets +20 HP for each Fighting Energy attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=CraftsmanshipPassive(),
        ),
        Attack(
            title="Top Down",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=top_down,
        ),
    ],
)
