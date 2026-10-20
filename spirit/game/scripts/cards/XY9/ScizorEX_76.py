from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import bonus_if


card = PokemonCardDef(
    guid="f992c92b-170e-5311-85f1-f28341ce3c8b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorEX.Name",
    display_name="Scizor-EX",
    searchable_by=["Scizor-EX", "Basic", "EX", "ScizorEX"],
    subtypes=["Basic", "EX"],
    collector_number=76,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=212,
    abilities=[
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Gale Thrust",
            game_text="If this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, this attack does 60 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.entered_active_this_turn(ctx.attacker), 60),
        ),
    ],
)