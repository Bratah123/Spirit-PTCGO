from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc057a12-def2-5b04-b8d5-42a44e7da160",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatVMAX.Name",
    display_name="Crobat VMAX",
    searchable_by=["Crobat VMAX", "VMAX", "CrobatVMAX"],
    subtypes=["VMAX"],
    collector_number=45,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatV.Name",
    family_id=169,
    abilities=[
        Attack(
            title="Stealth Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Max Cutter",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)