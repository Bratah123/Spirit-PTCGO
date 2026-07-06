from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90f22b55-270b-53f4-8f60-26020942ee66",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandacondaV.Name",
    display_name="Sandaconda V",
    searchable_by=["Sandaconda V", "Basic", "V", "SandacondaV"],
    subtypes=["Basic", "V"],
    collector_number=184,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=844,
    abilities=[
        Attack(
            title="Sand Eater",
            game_text="Attach a Fighting Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Sand Breath",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)