from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="2d173d0c-3394-5c28-b833-b743100a2301",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reuniclus.Name",
    display_name="Reuniclus",
    searchable_by=["Reuniclus", "Stage 2", "Reuniclus"],
    subtypes=["Stage 2"],
    collector_number=57,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duosion.Name",
    family_id=577,
    abilities=[
        Ability(
            title="Damage Swap",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Psywave",
            game_text="Does 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)