from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="54549d34-58f5-5bac-a9de-70786d136caf",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MagnezoneV.Name",
    display_name="Magnezone V",
    searchable_by=["Magnezone V", "Basic", "V", "MagnezoneV"],
    subtypes=["Basic", "V"],
    collector_number=175,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=462,
    abilities=[
        Attack(
            title="Magnetic Tension",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon. This attack does 40 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=gust_attack(damage_to_new_active=40, damage_before=0),
        ),
        Attack(
            title="Splitting Beam",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=snipe_attack(30, pool="bench", count=2, also_base=True),
        ),
    ],
)