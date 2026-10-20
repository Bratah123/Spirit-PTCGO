from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive, carrier_pokemon


class _ToolboxPassive(Passive):
    """This Pokemon may have up to 4 Pokemon Tool cards attached to it."""

    def tool_capacity(self, pokemon, carrier):
        return 4 if pokemon is carrier_pokemon(carrier) else 1


card = PokemonCardDef(
    guid="93e46875-45e9-54e8-bb63-d8e5bb07d720",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=561,
    abilities=[
        Ability(
            title="Toolbox",
            game_text="This Pok\u00e9mon may have up to 4 Pok\u00e9mon Tool cards attached to it. (If this Pok\u00e9mon loses this Ability, discard Pok\u00e9mon Tool cards attached to this Pok\u00e9mon until only 1 Pok\u00e9mon Tool card remains.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_ToolboxPassive(),
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)