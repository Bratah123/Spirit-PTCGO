from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.ecard import is_basic_non_baby, unused_energy_bonus


card = PokemonCardDef(
    guid="4a25dcee-27f1-5865-98a7-6ca10ed17dcd",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Dense Body",
            game_text="Any damage done to Slowbro by attacks from Basic Pok\u00e9mon (excluding Baby Pok\u00e9mon) is reduced by 20.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=takes_less_passive(20, attacker_pred=is_basic_non_baby),
        ),
        Attack(
            title="Energy Cannon",
            game_text="This attack does 30 damage plus 10 damage for each Energy attached to Slowbro but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unused_energy_bonus(per=10, cap=20),
        ),
    ],
)
