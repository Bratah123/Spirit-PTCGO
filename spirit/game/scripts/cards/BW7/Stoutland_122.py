from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="71279cd3-037c-5af4-b564-093e1ac5761a",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=122,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Ability(
            title="Sentinel",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent can't play any Supporter cards from his or her hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=unimplemented,
        ),
    ],
)