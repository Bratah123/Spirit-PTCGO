from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.session.effects import plasma_energy_attached


card = PokemonCardDef(
    guid="fd958cac-67a7-5241-b0ea-8fb2396b559b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TornadusEX.Name",
    display_name="Tornadus-EX",
    searchable_by=["Tornadus-EX", "Basic", "EX", "Team Plasma", "TornadusEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=114,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=641,
    abilities=[
        Attack(
            title="Windfall",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=shuffle_hand_into_deck_draw(6),
        ),
        Attack(
            title="Jet Blast",
            game_text="This attack does 30 more damage for each Plasma Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=damage_per(lambda ctx: len(plasma_energy_attached(ctx.attacker)), 30, base=60),
        ),
    ],
)