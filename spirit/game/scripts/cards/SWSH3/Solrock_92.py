from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import no_resistance_passive


def _lunatone_in_play(calc, carrier):
    if calc.attacker is None or carrier.owning_player_id != calc.attacker.owning_player_id:
        return False
    return any(
        p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Lunatone"
        for p in calc.board.pokemon_in_play(carrier.owning_player_id)
    )


card = PokemonCardDef(
    guid="fa37c045-f9e9-5767-b415-7b5d9ee608b6",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name",
    display_name="Solrock",
    searchable_by=["Solrock", "Basic", "Solrock"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=338,
    abilities=[
        Ability(
            title="Resistance Shade",
            game_text="If you have Lunatone in play, your opponent's Pok\u00e9mon in play have no Resistance.",
            passive=no_resistance_passive(when=_lunatone_in_play),
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)