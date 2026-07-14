from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_bench, damage_per
from spirit.game.card_effects.passives_common import prevent_damage_when


def _v_attack_on_carrier(calc, carrier) -> bool:
    return (
        calc.target is carrier
        and calc.attacker is not None
        and is_pokemon_v(calc.attacker.archetype_id)
    )


card = PokemonCardDef(
    guid="ec687afe-5c9c-5062-af4d-dc3f3f51211b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Ability(
            title="Miracle Body",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon V.",
            passive=prevent_damage_when(_v_attack_on_carrier),
        ),
        Attack(
            title="Rout",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 20, base=10),
        ),
    ],
)