from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="908bcbb5-587d-5280-b8da-085aae18766f",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MalamarV.Name",
    display_name="Malamar V",
    searchable_by=["Malamar V", "Basic", "V", "MalamarV"],
    subtypes=["Basic", "V"],
    collector_number=121,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=687,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. This attack does 30 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=gust_attack(damage_to_new_active=30),
        ),
        Attack(
            title="Brain Shake",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)