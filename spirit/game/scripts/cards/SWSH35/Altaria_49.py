from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.card_effects.pokemon import is_pokemon_gx


def _v_or_gx_attack_on_carrier(calc, carrier) -> bool:
    return (
        calc.target is carrier
        and calc.attacker is not None
        and (is_pokemon_v(calc.attacker.archetype_id) or is_pokemon_gx(calc.attacker.archetype_id))
    )


card = PokemonCardDef(
    guid="15143446-31a6-5341-b5aa-670dd522342d",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Miraculous Charm",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon V and Pok\u00e9mon-GX.",
            passive=prevent_damage_when(_v_or_gx_attack_on_carrier),
        ),
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)