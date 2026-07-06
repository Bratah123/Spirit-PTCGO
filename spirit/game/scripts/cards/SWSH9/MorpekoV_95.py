from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7abb821-e08c-53c8-8fc2-bab16f56b165",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MorpekoV.Name",
    display_name="Morpeko V",
    searchable_by=["Morpeko V", "Basic", "V", "MorpekoV"],
    subtypes=["Basic", "V"],
    collector_number=95,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Gnaw and Run",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Hangry Spike",
            game_text="If you played Marnie's Pride from your hand during this turn, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)