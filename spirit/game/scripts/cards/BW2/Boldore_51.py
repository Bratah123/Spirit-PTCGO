from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _has_fighting_resistance(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and \
        defender.get_attribute(AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value


card = PokemonCardDef(
    guid="b42c7416-1a32-5622-a5a6-f63edd5c5d33",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    display_name="Boldore",
    searchable_by=["Boldore", "Stage 1", "Boldore"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Smack Down",
            game_text="If the Defending Pok\u00e9mon has Fighting Resistance, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_has_fighting_resistance, 60),
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
