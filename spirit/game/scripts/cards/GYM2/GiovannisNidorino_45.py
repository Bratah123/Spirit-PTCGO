from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


card = PokemonCardDef(
    guid="7b0beefa-273c-5ce7-8fad-86f9d246dbcd",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidorino.Name",
    display_name="Giovanni's Nidorino",
    searchable_by=["Giovanni's Nidorino", "Stage 1", "GiovannisNidorino"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoran.Name",
    family_id=32,
    abilities=[
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 20 damage plus 20 more damage. If not, this attack does 20 damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bonus_if(has_damage("defender"), 20),
        ),
    ],
)
