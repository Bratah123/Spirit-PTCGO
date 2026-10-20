from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="984e76c7-7d6b-5220-82d4-97925004b7c2",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Team Plasma", "Hydreigon"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=78,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Tractorbeam",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. This attack does 40 damage to the new Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Obsidian Fang",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
    ],
)