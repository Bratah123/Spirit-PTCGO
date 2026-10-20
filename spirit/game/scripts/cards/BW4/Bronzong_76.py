from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_hand
from spirit.game.card_effects.passives_common import healing_block_passive


card = PokemonCardDef(
    guid="a126bc48-c8ba-5976-bd95-db6f8bd670c5",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(
            title="Heal Block",
            game_text="Damage can't be healed from any Pok\u00e9mon (both yours and your opponent's). (Damage counters can still be moved.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=healing_block_passive(lambda target, carrier: True),
        ),
        Attack(
            title="Oracle Inflict",
            game_text="Does 10 more damage for each card in your opponent's hand.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_hand('opponent'), 10, base=30),
        ),
    ],
)