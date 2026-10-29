from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard


card = PokemonCardDef(
    guid="f2238040-2e03-5929-9af6-26f8b432f487",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=86,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Energy Link",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=attach_from_discard(),
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
        ),
    ],
)