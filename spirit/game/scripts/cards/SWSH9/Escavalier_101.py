from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.passives_common import takes_less_passive


def _is_v(pokemon) -> bool:
    return is_pokemon_v(pokemon.archetype_id)

card = PokemonCardDef(
    guid="c591b00e-62d0-53bd-96df-bb6291f7740f",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier", "Stage 1", "Escavalier"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Ability(
            title="Miraculous Armor",
            game_text="This Pok\u00e9mon takes 100 less damage from attacks from your opponent's Pok\u00e9mon V (after applying Weakness and Resistance).",
            passive=takes_less_passive(100, attacker_pred=_is_v),
        ),
        Attack(
            title="Pike",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=snipe_attack(30, pool="bench", count=1, also_base=True),
        ),
    ],
)