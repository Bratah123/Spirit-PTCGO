from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import is_pokemon_gx
from spirit.game.card_effects.attacks_common import snipe_attack


def _deep_forest_camo_pred(calc, carrier):
    if calc.target is not carrier or calc.attacker is None:
        return False
    atk_id = calc.attacker.archetype_id
    return is_pokemon_v(atk_id) or is_pokemon_gx(atk_id)


card = PokemonCardDef(
    guid="7024b910-8cfd-5096-bee9-77c505f96e64",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueye.Name",
    display_name="Decidueye",
    searchable_by=["Decidueye", "Stage 2", "Decidueye"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Deep Forest Camo",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon V and Pok\u00e9mon-GX.",
            passive=prevent_damage_when(_deep_forest_camo_pred),
        ),
        Attack(
            title="Splitting Arrow",
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=snipe_attack(20, pool="bench", count=2, also_base=True),
        ),
    ],
)