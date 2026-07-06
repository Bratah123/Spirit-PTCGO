from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0687700d-989d-53dc-9dda-644b5798ea5f",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminVSTAR.Name",
    display_name="Shaymin VSTAR",
    searchable_by=["Shaymin VSTAR", "VSTAR", "ShayminVSTAR"],
    subtypes=["VSTAR"],
    collector_number=173,
    set_code="SWSH9",
    rarity=Rarities.RareRainbow,
    hp=250,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminV.Name",
    family_id=492,
    abilities=[
        Ability(
            title="Star Bloom",
            game_text="During your turn, you may heal 120 damage from each of your Benched Grass Pok\u00e9mon. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 40 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)