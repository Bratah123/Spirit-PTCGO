from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import metal_burn_discard_all_metal, peal_of_thunder_on_evolve

card = PokemonCardDef(
    guid="79bc3105-ecf7-5ec3-a49b-75e03b0ce7b1",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard δ",
    searchable_by=["Charizard \u03b4", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Peal of Thunder",
            game_text="Once during your turn, when you play Charizard from your hand to evolve 1 of your Pok\u00e9mon, you may look at the top 5 cards of your deck, choose as many Energy cards as you like, and attach them to 1 of your Pok\u00e9mon. Discard the other cards.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
                        effect=peal_of_thunder_on_evolve(30),
        ),
        Attack(
            title="Metal Burn",
            game_text="Discard all Metal Energy attached to Charizard.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
                        effect=metal_burn_discard_all_metal(),
        ),
    ],
)