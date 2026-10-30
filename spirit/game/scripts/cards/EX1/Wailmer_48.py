from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import rest_attack
from spirit.game.card_effects.ex import extra_energy_damage


card = PokemonCardDef(
    guid="c76c129c-3f5f-5ec2-8457-8ec3a171809f",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    display_name="Wailmer",
    searchable_by=["Wailmer", "Basic", "Wailmer"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=320,
    abilities=[
        Attack(
            title="Rest",
            game_text="Remove all Special Conditions and 4 damage counters from Wailmer (all if there are less than 4). Wailmer is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=rest_attack(4),
        ),
        Attack(
            title="Water Gun",
            game_text="This attack does 20 damage plus 10 more damage for each Water Energy attached to Wailmer but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=extra_energy_damage(
                10, base=20, extra_cap=2, energy_type=PokemonTypes.WATER,
            ),
        ),
    ],
)
