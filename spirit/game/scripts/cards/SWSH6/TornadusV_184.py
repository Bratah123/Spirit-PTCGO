from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6e6cd69-b2d0-5ad9-99f9-00e9e3656cfc",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusV.Name",
    display_name="Tornadus V",
    searchable_by=["Tornadus V", "Basic", "V", "Single Strike", "TornadusV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=184,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=641,
    abilities=[
        Attack(
            title="Blow Through",
            game_text="If a Stadium is in play, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Blasting Hammer",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=180,
            effect=unimplemented,
        ),
    ],
)