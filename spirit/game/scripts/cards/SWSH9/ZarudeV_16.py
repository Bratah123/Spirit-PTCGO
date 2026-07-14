from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, snipe_attack, defender_is_v

card = PokemonCardDef(
    guid="13b89f67-e10e-5a0c-b5a0-0ffa88ab20f7",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZarudeV.Name",
    display_name="Zarude V",
    searchable_by=["Zarude V", "Basic", "V", "ZarudeV"],
    subtypes=["Basic", "V"],
    collector_number=16,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Leap to Leap",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=snipe_attack(30, pool="bench", count=1, also_base=True),
        ),
        Attack(
            title="Jungle Rage",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 120 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=bonus_if(defender_is_v, 120),
        ),
    ],
)