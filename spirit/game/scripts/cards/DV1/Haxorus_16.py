from spirit.game.card_effects.attacks_common import bonus_if, mill_attack
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _defender_is_colorless(ctx):
    defender = ctx.defender
    if defender is None:
        return False
    types = defender.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.COLORLESS.value in types


card = PokemonCardDef(
    guid="297ebda3-063e-536a-97a0-0f684b01e3c7",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="DV1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Axe Slugger",
            game_text="If the Defending Pok\u00e9mon is a Colorless Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_defender_is_colorless, 60),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=mill_attack(1, opponent=False),
        ),
    ],
)
