from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="16a3139c-3856-59e6-9fc5-d4fde8e82fca",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=137,
    set_code="BW8",
    rarity=Rarities.RareSecret,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=9,
    abilities=[
        Ability(
            title="Deluge",
            game_text="As often as you like during your turn (before your attack), you may attach a Water Energy card from your hand to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 10 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)