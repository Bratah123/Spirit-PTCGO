from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import bell_of_silence

card = PokemonCardDef(
    guid="16316e6f-1ee2-57f1-b82b-b99869e538f0",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=358,
    abilities=[
        Attack(
            title="Bell of Silence",
            game_text="Your opponent can't play any Pok\u00e9mon that has an Ability from their hand during their next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=bell_of_silence,
        ),
    ],
)