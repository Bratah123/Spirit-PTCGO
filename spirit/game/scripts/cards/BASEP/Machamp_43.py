from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, flip_damage
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="5c189c7a-e8f2-5794-905b-a650586bdb9d",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=68,
    abilities=[
        Attack(
            title="Seething Anger",
            game_text="Flip a number of coins equal to the number of damage counters on Machamp. This attack does 20 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins_from=damage_counters_on("self"), bonus_per_heads=10),
        ),
        Attack(
            title="Fling",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)
