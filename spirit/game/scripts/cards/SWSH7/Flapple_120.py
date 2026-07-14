from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_in_play, bonus_if, defender_is_v


def _has_ability(pokemon) -> bool:
    abilities = pokemon.get_attribute(AttrID.PIE_ABILITIES) or []
    return any(isinstance(e, dict) and e.get("abilityType") in ("PokeAbility", "PokePower")
               for e in abilities)


card = PokemonCardDef(
    guid="b37d682c-193f-5d1d-b36a-06a5eae44cc8",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flapple.Name",
    display_name="Flapple",
    searchable_by=["Flapple", "Stage 1", "Flapple"],
    subtypes=["Stage 1"],
    collector_number=120,
    set_code="SWSH7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Acidic Mucus",
            game_text="This attack does 50 damage for each of your opponent's Pok\u00e9mon in play that has an Ability.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_in_play("opponent", _has_ability), 50),
        ),
        Attack(
            title="Fighting Tackle",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(defender_is_v, 80),
        ),
    ],
)