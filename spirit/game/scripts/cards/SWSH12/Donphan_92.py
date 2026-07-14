from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def overspin(ctx):
    state = ctx.session.turn_state
    if state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number:
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="eb78afbe-8fda-5b51-a486-dc74f3b1a34a",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Overspin",
            game_text="If this Pok\u00e9mon evolved during this turn, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=110,
            effect=overspin,
        ),
        Attack(
            title="Giant Fangs",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=170,
        ),
    ],
)