from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6ed1b3e8-c46e-5abd-8941-8efe6dab32e7",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexVMAX.Name",
    display_name="Shadow Rider Calyrex VMAX",
    searchable_by=["Shadow Rider Calyrex VMAX", "VMAX", "ShadowRiderCalyrexVMAX"],
    subtypes=["VMAX"],
    collector_number=204,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    hp=320,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ShadowRiderCalyrexV.Name",
    family_id=898,
    abilities=[
        Ability(
            title="Underworld Door",
            game_text="Once during your turn, you may attach a Psychic Energy card from your hand to 1 of your Benched Psychic Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, draw 2 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Max Geist",
            game_text="This attack does 30 more damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)