from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import discard_then_draw
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="c033b410-8ffe-587e-9ff0-60d5858dbf6e",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TalonflameV.Name",
    display_name="Talonflame V",
    searchable_by=["Talonflame V", "Basic", "V", "TalonflameV"],
    subtypes=["Basic", "V"],
    collector_number=168,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=663,
    abilities=[
        Attack(
            title="Fast Flight",
            game_text="If you go first, you can use this attack during your first turn. Discard your hand and draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            usable_first_turn=True,
            effect=discard_then_draw(None, 6, whole_hand=True),
        ),
        Attack(
            title="Bright Wing",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)