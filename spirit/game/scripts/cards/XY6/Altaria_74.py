from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.passives_common import no_weakness_passive


def _my_colorless(target, carrier):
    return (target.owning_player_id == carrier.owning_player_id
            and PokemonTypes.COLORLESS.value in (target.get_attribute(AttrID.POKEMON_TYPES) or []))


card = PokemonCardDef(
    guid="8c000f05-df56-5ba1-bc08-7b3156365cc3",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name",
    display_name="Altaria",
    searchable_by=["Altaria", "Stage 1", "Altaria"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Ability(
            title="Clear Humming",
            game_text="Each of your Colorless Pok\u00e9mon has no Weakness.",
            passive=no_weakness_passive(_my_colorless),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)