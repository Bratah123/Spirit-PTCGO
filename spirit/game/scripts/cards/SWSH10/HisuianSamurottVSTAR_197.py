from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a0cbc59-d52b-5cb0-b1c2-13f79ea5e104",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurottVSTAR.Name",
    display_name="Hisuian Samurott VSTAR",
    searchable_by=["Hisuian Samurott VSTAR", "VSTAR", "HisuianSamurottVSTAR"],
    subtypes=["VSTAR"],
    collector_number=197,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianSamurottV.Name",
    family_id=503,
    abilities=[
        Ability(
            title="Moon Cleave Star",
            game_text="During your turn, you may put 4 damage counters on 1 of your opponent's Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Merciless Blade",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 110 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=110,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)