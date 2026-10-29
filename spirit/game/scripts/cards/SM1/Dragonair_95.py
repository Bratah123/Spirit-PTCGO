from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _dragons_wish(ctx):
    """During your next turn, you may attach any number of Energy cards from your hand."""
    state = ctx.session.turn_state
    state.allow_unlimited_energy_attach(ctx.player_id, state.turn_number + 2)


card = PokemonCardDef(
    guid="18473d67-e595-5a49-a325-0480d38dad4b",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Dragon's Wish",
            game_text="During your next turn, you may attach any number of Energy cards from your hand to your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_dragons_wish,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)