from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75f1df96-2e2a-506d-b0f8-ebb1a8630804",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    display_name="Corvisquire",
    searchable_by=["Corvisquire", "Stage 1", "Corvisquire"],
    subtypes=["Stage 1"],
    collector_number=151,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Pluck",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)