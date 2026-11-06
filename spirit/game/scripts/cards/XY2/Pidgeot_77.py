from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="480987bc-e278-517b-93c7-fa414c0bb51a",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name",
    display_name="Pidgeot",
    searchable_by=["Pidgeot", "Stage 2", "Pidgeot"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Strong Gust",
            game_text="During your next turn, this Pok\u00e9mon's Strong Gust attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=boost_own_next_turn(60, attack_title='Strong Gust'),
        ),
    ],
)