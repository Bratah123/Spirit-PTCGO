from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import hard_rock_low_energy, power_blast_discard_energy

card = PokemonCardDef(
    guid="4d3483e4-6ff8-5fb4-87c8-8340e26ff1c3",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "ex", "Groudonex"],
    subtypes=["Basic", "ex"],
    collector_number=93,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Ability(
            title="Hard Rock",
            game_text="As long as Groudon ex has 1 Energy or less attached to it, damage done to any of your Groudon ex in play by attacks is reduced by 20 (after applying Weakness and Resistance). You can't use more than 1 Hard Rock Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=hard_rock_low_energy(20),
            effect=None,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard 2 Energy attached to Groudon ex.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
                        effect=power_blast_discard_energy(2),
        ),
    ],
)