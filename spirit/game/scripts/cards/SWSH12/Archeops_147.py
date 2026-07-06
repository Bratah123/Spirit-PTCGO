from spirit.game.card_effects.pokemon import primal_turbo
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1ff4ef4-88a9-5f17-b940-0194d40dff6f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archeops.Name",
    display_name="Archeops",
    searchable_by=["Archeops", "Stage 2", "Archeops"],
    subtypes=["Stage 2"],
    collector_number=147,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Archen.Name",
    family_id=566,
    abilities=[
        Ability(
            title="Primal Turbo",
            game_text="Once during your turn, you may search your deck for up to 2 Special Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=primal_turbo,
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)
