from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mirror_move, mirror_move_condition
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="57689080-4141-5976-8326-ffb1fcbbf4c4",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    display_name="Pidgeotto",
    searchable_by=["Pidgeotto", "Stage 1", "Pidgeotto"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Mirror Move",
            game_text="If Pidgeotto was attacked last turn, do the final result of that attack on Pidgeotto to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            condition=mirror_move_condition,
            effect=mirror_move,
        ),
    ],
)
