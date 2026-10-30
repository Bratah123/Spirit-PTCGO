from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import sludge_grip


card = PokemonCardDef(
    guid="48c0e814-29d6-5320-906d-ccd0cf961370",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasGrimer.Name",
    display_name="Koga's Grimer",
    searchable_by=["Koga's Grimer", "Basic", "KogasGrimer"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Sludge Grip",
            game_text="If your opponent has any Benched Pok\u00e9mon, flip a coin. If heads, choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon. The new Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=sludge_grip,
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
