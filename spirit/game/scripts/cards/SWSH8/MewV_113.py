from spirit.game.card_effects.pokemon import energy_mix, psychic_leap
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf0556da-f2cd-5b45-8bd9-6b7bff65f745",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewV.Name",
    display_name="Mew V",
    searchable_by=["Mew V", "Basic", "V", "Fusion Strike", "MewV"],
    subtypes=["Basic", "V", "Fusion Strike"],
    collector_number=113,
    set_code="SWSH8",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    abilities=[
        Attack(
            title="Energy Mix",
            game_text="Search your deck for an Energy card and attach it to 1 of your Fusion Strike Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=energy_mix,
        ),
        Attack(
            title="Psychic Leap",
            game_text="You may shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=psychic_leap,
        ),
    ],
)