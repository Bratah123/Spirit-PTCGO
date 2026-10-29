from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.session.passives import Passive


class WagesOfFluffPassive(Passive):
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is carrier:
            return count + 2
        return count


async def wages_of_fluff(ctx):
    """If the Defending Pokémon is KO'd during your next turn, take 2 more prizes."""
    defender = ctx.defender
    if defender is not None:
        ctx.add_passive_through_own_next_turn(defender, WagesOfFluffPassive())


card = PokemonCardDef(
    guid="e4459670-cc29-58e9-82a2-e010e4fceba2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="The Wages of Fluff",
            game_text="If the Defending Pok\u00e9mon is Knocked Out during your next turn, take 2 more Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=wages_of_fluff,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
        ),
    ],
)