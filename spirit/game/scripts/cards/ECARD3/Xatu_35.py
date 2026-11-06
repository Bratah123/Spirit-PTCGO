from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import SynchronicityPassive, warp_hole


card = PokemonCardDef(
    guid="08aec4f6-ae6f-5ee5-9599-0b009ea487c8",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Ability(
            title="Synchronicity",
            game_text="You may attach any Technical Machine to Xatu.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=SynchronicityPassive(),
        ),
        Attack(
            title="Warp Hole",
            game_text="Flip a coin. If heads, choose a card from your discard pile and put it on top of your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=warp_hole,
        ),
    ],
)
