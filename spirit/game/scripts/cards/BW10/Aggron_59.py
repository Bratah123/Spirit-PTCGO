from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="037f1448-ddb7-575a-b700-0c6339d53f39",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2", "Aggron"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Knock Back",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Aura of the Land",
            game_text="Does 20 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=spread_damage(20, side='both', also_base=True),
        ),
    ],
)