from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import evolutionary_spore


card = PokemonCardDef(
    guid="f8811f3d-a10a-5c97-a17e-501763385f61",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name",
    display_name="Jumpluff",
    searchable_by=["Jumpluff", "Stage 2", "Jumpluff"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    family_id=188,
    abilities=[
        Attack(
            title="Evolutionary Spore",
            game_text="Choose any number of your Hoppips and Skiplooms. Then, for each Pok\u00e9mon you chose in this way, you may search your deck for a card that evolves from that Pok\u00e9mon and attach it to that Pok\u00e9mon. (This counts as evolving those Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=evolutionary_spore,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
