from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="040f2a64-dffa-52b3-8248-30a1faacf403",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpixVSTAR.Name",
    display_name="Alolan Vulpix VSTAR",
    searchable_by=["Alolan Vulpix VSTAR", "VSTAR", "AlolanVulpixVSTAR"],
    subtypes=["VSTAR"],
    collector_number=34,
    set_code="SWSH12",
    rarity=Rarities.RareHoloVSTAR,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpixV.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Snow Mirage",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon that have an Ability.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
        Attack(
            title="Silvery Snow Star",
            game_text="This attack does 70 damage for each of your opponent's Pok\u00e9mon V in play. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 VSTAR Power in a game.)",
            cost={},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)