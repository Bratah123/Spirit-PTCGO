from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, flip_damage


def _kos_suffered_last_turn(ctx):
    return ctx.kos_suffered_last_turn() > 0


card = PokemonCardDef(
    guid="eba91c76-acef-576e-8fd1-37bbcf223366",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Attack(
            title="Revenge",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an opponent's attack during his or her last turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_kos_suffered_last_turn, 70),
        ),
        Attack(
            title="Head Charge",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=flip_damage(tails_self_damage=20),
        ),
    ],
)
